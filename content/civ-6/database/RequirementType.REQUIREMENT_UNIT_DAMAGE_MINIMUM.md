---
tags:
- RequirementType
title: REQUIREMENT_UNIT_DAMAGE_MINIMUM
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_DAMAGE_MINIMUM
>
> * Class: `UNITS`
> * Arguments:
>	* MinimumAmount `Integer`

## Samples

```SQL {title="OPPONENT_IS_DAMAGED_UNIT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"OPPONENT_IS_DAMAGED_UNIT_REQUIREMENT",
		"REQUIREMENT_UNIT_DAMAGE_MINIMUM"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"OPPONENT_IS_DAMAGED_UNIT_REQUIREMENT",
		"MinimumAmount",
		1
	);
	```
