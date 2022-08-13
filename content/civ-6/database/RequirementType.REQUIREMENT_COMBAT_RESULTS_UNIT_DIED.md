---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_RESULTS_UNIT_DIED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_RESULTS_UNIT_DIED
>
> * Class: `Unknown`
> * Arguments:
>	* OnlyBarbs `Unknown`
>	* ExcludeBarbs `Unknown`

## Samples

```SQL {title="REQUIRE_THIS_COMBAT_RESULTS_IN_UNIT_DEATH"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRE_THIS_COMBAT_RESULTS_IN_UNIT_DEATH",
		"REQUIREMENT_COMBAT_RESULTS_UNIT_DIED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRE_THIS_COMBAT_RESULTS_IN_UNIT_DEATH",
		"ExcludeBarbs",
		1
	);
	```

```SQL {title="REQUIRE_THIS_COMBAT_RESULTS_IN_BARB_UNIT_DEATH"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRE_THIS_COMBAT_RESULTS_IN_BARB_UNIT_DEATH",
		"REQUIREMENT_COMBAT_RESULTS_UNIT_DIED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRE_THIS_COMBAT_RESULTS_IN_BARB_UNIT_DEATH",
		"OnlyBarbs",
		1
	);
	```
