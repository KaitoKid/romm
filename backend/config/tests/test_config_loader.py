import os
from pathlib import Path

from config.config_loader import ConfigLoader


def test_config_loader():
    loader = ConfigLoader(
        os.path.join(Path(__file__).resolve().parent, "fixtures", "config.yml")
    )

    assert loader.config.EXCLUDED_PLATFORMS == ["romm"]
    assert loader.config.EXCLUDED_SINGLE_EXT == ["xml"]
    assert loader.config.EXCLUDED_SINGLE_FILES == ["info.txt"]
    assert loader.config.EXCLUDED_MULTI_FILES == ["my_multi_file_game", "DLC"]
    assert loader.config.EXCLUDED_MULTI_PARTS_EXT == ["txt"]
    assert loader.config.EXCLUDED_MULTI_PARTS_FILES == ["data.xml"]
    assert loader.config.PLATFORMS_BINDING == {"gc": "ngc"}
    assert loader.config.ROMS_FOLDER_NAME == "ROMS"
    assert loader.config.SAVES_FOLDER_NAME == "SAVES"
    assert loader.config.STATES_FOLDER_NAME == "STATES"
    assert loader.config.SCREENSHOTS_FOLDER_NAME == "SCREENSHOTS"


def test_empty_config_loader():
    loader = ConfigLoader("")

    assert loader.config.EXCLUDED_PLATFORMS == []
    assert loader.config.EXCLUDED_SINGLE_EXT == []
    assert loader.config.EXCLUDED_SINGLE_FILES == []
    assert loader.config.EXCLUDED_MULTI_FILES == []
    assert loader.config.EXCLUDED_MULTI_PARTS_EXT == []
    assert loader.config.EXCLUDED_MULTI_PARTS_FILES == []
    assert loader.config.PLATFORMS_BINDING == {}
    assert loader.config.ROMS_FOLDER_NAME == "roms"
    assert loader.config.SAVES_FOLDER_NAME == "saves"
    assert loader.config.STATES_FOLDER_NAME == "states"
    assert loader.config.SCREENSHOTS_FOLDER_NAME == "screenshots"
