import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import generate_mondo


def response(json_data=None, content=b""):
    mocked = Mock()
    mocked.json.return_value = json_data
    mocked.content = content
    mocked.raise_for_status.return_value = None
    return mocked


class AtlasImageTests(unittest.TestCase):
    @patch.dict("os.environ", {"ATLASCLOUD_API_KEY": "test-key"}, clear=True)
    @patch("generate_mondo.time.sleep")
    @patch("generate_mondo.requests.get")
    @patch("generate_mondo.requests.post")
    def test_submits_once_polls_and_downloads(self, post, get, _sleep):
        post.return_value = response({"data": {"id": "prediction-1"}})
        get.side_effect = [
            response({"data": {"status": "processing"}}),
            response({
                "data": {
                    "status": "completed",
                    "outputs": ["https://cdn.example.com/poster.png"],
                }
            }),
            response(content=b"image-bytes"),
        ]

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "poster.png"
            result = generate_mondo.generate_atlas_image(
                "a poster", str(output), max_polls=3, poll_interval=0
            )

            self.assertEqual(result, str(output))
            self.assertEqual(output.read_bytes(), b"image-bytes")

        self.assertEqual(post.call_count, 1)
        self.assertEqual(get.call_count, 3)
        self.assertEqual(
            post.call_args.kwargs["json"],
            {
                "model": generate_mondo.ATLAS_DEFAULT_MODEL,
                "prompt": "a poster",
                "aspect_ratio": "9:16",
                "resolution": "1k",
            },
        )

    @patch.dict("os.environ", {"ATLASCLOUD_API_KEY": "test-key"}, clear=True)
    @patch("generate_mondo.requests.post")
    def test_rejects_unsupported_ratio_before_submit(self, post):
        result = generate_mondo.generate_atlas_image("a poster", aspect_ratio="7:5")

        self.assertIsNone(result)
        post.assert_not_called()


if __name__ == "__main__":
    unittest.main()
