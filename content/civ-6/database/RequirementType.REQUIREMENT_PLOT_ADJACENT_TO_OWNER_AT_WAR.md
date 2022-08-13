---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_TO_OWNER_AT_WAR
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_TO_OWNER_AT_WAR
>
> * Class: `PLOTS`
> * Arguments:
>	* MinDistance `Integer`
>	* MaxDistance `Integer`

## Samples

```SQL {title="REQUIRE_THIS_UNIT_IS_ADJACENT_AND_AT_WAR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRE_THIS_UNIT_IS_ADJACENT_AND_AT_WAR",
		"REQUIREMENT_PLOT_ADJACENT_TO_OWNER_AT_WAR"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRE_THIS_UNIT_IS_ADJACENT_AND_AT_WAR",
		"MaxDistance",
		1
	),
	(
		"REQUIRE_THIS_UNIT_IS_ADJACENT_AND_AT_WAR",
		"MinDistance",
		1
	);
	
```
