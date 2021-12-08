import unittest
from haversine import haversine
from tramdata import *

# extra tests to help grading

STOPS_PATH = "../data/tramstops.json"
LINES_PATH = "../data/tramlines.txt"

class TestCase(unittest.TestCase):
    def test_build_tram_stops(self):
        stops_dict = build_tram_stops(STOPS_PATH)
        assert len(stops_dict.keys()) == 133
        assert stops_dict["Majvallen"]["lat"] == 57.6909343
        assert stops_dict["Majvallen"]["lon"] == 11.9354935

    def test_line_dict(self):
        (line_dict,_) = build_tram_lines(LINES_PATH)
        assert len(line_dict.keys()) == 12 # no, not 13! 12 is missing
        assert line_dict["9"][0] == "Angered Centrum"
        assert line_dict["9"][-1] == "Kungssten"
        assert "10" in line_dict.keys()
        with self.assertRaises(KeyError):
            line_dict["12"]

    def test_time_dict(self):
        (_,time_dict) = build_tram_lines(LINES_PATH)
        assert time_dict["Kviberg"]["Beväringsgatan"] == 1
        assert time_dict["Beväringsgatan"]["Kviberg"] == time_dict["Kviberg"]["Beväringsgatan"]
        with self.assertRaises(KeyError):
            time_dict["Brunnsparken"]["Chalmers"] # they are not adjacent
        assert len(time_dict["Brunnsparken"].keys()) == 6

    def test_lines_via_stop(self):
        (lines_dict,_) = build_tram_lines(LINES_PATH)
        beväringsgatan_lines = lines_via_stop(lines_dict, "Beväringsgatan")
        assert set(beväringsgatan_lines) == set(['6', '7', '11'])
        assert beväringsgatan_lines == ['6', '7', '11']
        assert lines_via_stop(lines_dict, "Beväringsgatan") == ['6', '7', '11']
        assert lines_via_stop(lines_dict, "Via Coriolano Monti") == []

    def test_lines_between_stops(self):
        (lines_dict,_) = build_tram_lines(LINES_PATH)
        assert lines_between_stops(lines_dict, "Kviberg", "Chalmers") == ['6', '7']
        assert lines_between_stops(lines_dict, "Kviberg", "Chalmers") == lines_between_stops(lines_dict, "Chalmers", "Kviberg")

    def test_time_between_stops(self):
        (lines_dict,times_dict) = build_tram_lines(LINES_PATH)
        assert time_between_stops(lines_dict, times_dict, "6", "Beväringsgatan","Chalmers") == 22
        assert time_between_stops(lines_dict, times_dict, "6", "Chalmers","Beväringsgatan") == 22
        assert time_between_stops(lines_dict, times_dict, "6", "Beväringsgatan","Beväringsgatan") == 0
        assert time_between_stops(lines_dict, times_dict, "1", "Chalmers","Beväringsgatan") == None

    def test_distance_between_stops(self):
        stops_dict = build_tram_stops(STOPS_PATH)
        stop1 = "Chalmers"
        stop2 = "Kviberg"
        coords1 = (stops_dict[stop1]["lat"], stops_dict[stop1]["lon"])
        coords2 = (stops_dict[stop2]["lat"], stops_dict[stop2]["lon"])
        assert distance_between_stops(stops_dict, stop1, stop1) == 0
        dist = distance_between_stops(stops_dict, stop1, stop2)
        ref_dist = haversine(coords1, coords2)
        self.assertAlmostEqual(dist,ref_dist,places=2)