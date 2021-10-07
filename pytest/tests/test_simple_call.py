# coding=utf-8
""" Simple testing calling the Para-C CLI """
import parac_cli


class TestCall:

    def test_simple_pass(self):
        assert parac_cli.cli_entry
