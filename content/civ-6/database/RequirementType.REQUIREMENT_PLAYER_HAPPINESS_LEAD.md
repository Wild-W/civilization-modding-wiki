---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAPPINESS_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAPPINESS_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinimumDelta `Integer`
>	* HappinessRatio `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_HAPPINESS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_HAPPINESS",
		"REQUIREMENT_PLAYER_HAPPINESS_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_HAPPINESS",
		"HappinessRatio",
		"1.3"
	),
	(
		"REQUIRES_HAS_HIGH_HAPPINESS",
		"MinimumDelta",
		2
	);
	```
