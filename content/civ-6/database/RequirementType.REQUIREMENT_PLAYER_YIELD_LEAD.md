---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_YIELD_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_YIELD_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* YieldType `String`
>		* [Yields.YieldType]
>	* YieldRatio `Integer`
>	* MinimumDelta `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_CULTURE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_CULTURE",
		"REQUIREMENT_PLAYER_YIELD_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_CULTURE",
		"MinimumDelta",
		5
	),
	(
		"REQUIRES_HAS_HIGH_CULTURE",
		"YieldRatio",
		"1.15"
	),
	(
		"REQUIRES_HAS_HIGH_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	```
