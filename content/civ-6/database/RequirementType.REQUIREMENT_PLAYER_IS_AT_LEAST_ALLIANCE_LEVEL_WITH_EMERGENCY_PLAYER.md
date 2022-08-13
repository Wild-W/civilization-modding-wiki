---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_AT_LEAST_ALLIANCE_LEVEL_WITH_EMERGENCY_PLAYER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_AT_LEAST_ALLIANCE_LEVEL_WITH_EMERGENCY_PLAYER
>
> * Class: `PLAYERS`
> * Arguments:
>	* Level `Integer`

## Samples

```SQL {title="REQUIRES_HIGH_ALLIANCE_LEVEL_WITH_EMERGENCY_PLAYER_DATA"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HIGH_ALLIANCE_LEVEL_WITH_EMERGENCY_PLAYER_DATA",
		"REQUIREMENT_PLAYER_IS_AT_LEAST_ALLIANCE_LEVEL_WITH_EMERGENCY_PLAYER"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HIGH_ALLIANCE_LEVEL_WITH_EMERGENCY_PLAYER_DATA",
		"Level",
		2
	);
	
```
