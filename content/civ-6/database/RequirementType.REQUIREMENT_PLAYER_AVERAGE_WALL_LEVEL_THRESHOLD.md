---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_AVERAGE_WALL_LEVEL_THRESHOLD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_AVERAGE_WALL_LEVEL_THRESHOLD
>
> * Class: `PLAYERS`
> * Arguments:
>	* AverageWallLevelThreshold `Integer`
>	* AboveThreshold `Boolean`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_WALLS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_WALLS",
		"REQUIREMENT_PLAYER_AVERAGE_WALL_LEVEL_THRESHOLD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_WALLS",
		"AboveThreshold",
		1
	),
	(
		"REQUIRES_HAS_HIGH_WALLS",
		"AverageWallLevelThreshold",
		"1.0"
	);
	
```
