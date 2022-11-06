#!/usr/bin/env python

"""Tests for `deploy_42sol` package."""


import unittest
from click.testing import CliRunner

from deploy_42sol import deploy_42sol
from deploy_42sol import cli


class TestDeploy_42sol(unittest.TestCase):
    """Tests for `deploy_42sol` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'deploy_42sol.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
