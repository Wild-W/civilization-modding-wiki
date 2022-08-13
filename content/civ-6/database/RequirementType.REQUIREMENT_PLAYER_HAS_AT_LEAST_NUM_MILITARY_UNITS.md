---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_AT_LEAST_NUM_MILITARY_UNITS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_AT_LEAST_NUM_MILITARY_UNITS
>
> * Class: `PLAYERS`
> * Arguments:
>	* Amount `Integer`

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_SMALL_MILITARY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_SMALL_MILITARY",
		"REQUIREMENT_PLAYER_HAS_AT_LEAST_NUM_MILITARY_UNITS",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_SMALL_MILITARY",
		"Amount",
		10
	);
	```
