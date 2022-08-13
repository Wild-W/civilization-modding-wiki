---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_DIPLO_VP_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_DIPLO_VP_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* Ratio `Integer`
>	* MinimumDelta `Integer`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_DIPLOVP"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_DIPLOVP",
		"REQUIREMENT_PLAYER_DIPLO_VP_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_DIPLOVP",
		"MinimumDelta",
		1
	),
	(
		"REQUIRES_HAS_HIGH_DIPLOVP",
		"Ratio",
		"1.5"
	);
	```
