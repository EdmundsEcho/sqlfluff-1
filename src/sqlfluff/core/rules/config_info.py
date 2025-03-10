"""Documenting and validating rule configuration.

Provide a mapping with all configuration options, with information
on valid inputs and definitions.

This mapping is used to validate rule config inputs, as well
as document rule configuration.
"""

from sqlfluff.core.plugin.host import get_plugin_manager

STANDARD_CONFIG_INFO_DICT = {
    "tab_space_size": {
        "validation": range(100),
        "definition": (
            "The number of spaces to consider equal to one tab. "
            "Used in the fixing step of this rule"
        ),
    },
    "max_line_length": {
        "validation": range(1000),
        "definition": (
            "The maximum length of a line to allow without " "raising a violation"
        ),
    },
    "indent_unit": {
        "validation": ["space", "tab"],
        "definition": "Whether to use tabs or spaces to add new indents",
    },
    "comma_style": {
        "validation": ["leading", "trailing"],
        "definition": "The comma style to to enforce",
    },
    "allow_scalar": {
        "validation": [True, False],
        "definition": (
            "Whether or not to allow a single element in the "
            " select clause to be without an alias"
        ),
    },
    "single_table_references": {
        "validation": ["consistent", "qualified", "unqualified"],
        "definition": "The expectation for references in single-table select",
    },
    "unquoted_identifiers_policy": {
        "validation": ["all", "aliases", "column_aliases"],
        "definition": "Types of unquoted identifiers to flag violations for",
    },
    "capitalisation_policy": {
        "validation": ["consistent", "upper", "lower", "capitalise"],
        "definition": "The capitalisation policy to enforce",
    },
    "extended_capitalisation_policy": {
        "validation": ["consistent", "upper", "lower", "pascal", "capitalise"],
        "definition": (
            "The capitalisation policy to enforce, extended with PascalCase. "
            "This is separate from capitalisation_policy as it should not be "
            "applied to keywords."
        ),
    },
    "lint_templated_tokens": {
        "validation": [True, False],
        "definition": (
            "Should lines starting with a templating placeholder"
            " such as `{{blah}}` have their indentation linted"
        ),
    },
    "select_clause_trailing_comma": {
        "validation": ["forbid", "require"],
        "definition": (
            "Should trailing commas within select clauses be required or forbidden"
        ),
    },
    "ignore_comment_lines": {
        "validation": [True, False],
        "definition": (
            "Should lines that contain only whitespace and comments"
            " be ignored when linting line lengths"
        ),
    },
    "forbid_subquery_in": {
        "validation": ["join", "from", "both"],
        "definition": "Which clauses should be linted for subqueries",
    },
    "prefer_count_1": {
        "validation": [True, False],
        "definition": ("Should count(1) be preferred over count(*) and count(0)?"),
    },
    "prefer_count_0": {
        "validation": [True, False],
        "definition": ("Should count(0) be preferred over count(*) and count(1)?"),
    },
    "operator_new_lines": {
        "validation": ["before", "after"],
        "definition": ("Should operator be placed before or after newlines."),
    },
}


def get_config_info() -> dict:
    """Gets the config from core sqlfluff and sqlfluff plugins and merges them."""
    plugin_manager = get_plugin_manager()
    configs_info = plugin_manager.hook.get_configs_info()
    return {
        k: v for config_info_dict in configs_info for k, v in config_info_dict.items()
    }
