---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_INCOME_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_INCOME_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* YieldRatio `Integer`
>	* MinimumDelta `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_INCOME"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_INCOME",
		"REQUIREMENT_PLAYER_INCOME_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_INCOME",
		"MinimumDelta",
		10
	),
	(
		"REQUIRES_HAS_HIGH_INCOME",
		"YieldRatio",
		"1.3"
	);
	```
