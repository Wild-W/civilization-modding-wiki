---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_ACTIVE_ALLIANCE_OF_AT_LEAST_LEVEL
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_ACTIVE_ALLIANCE_OF_AT_LEAST_LEVEL
>
> * Class: `PLAYERS`
> * Arguments:
>	* Level `Integer`

## Samples

```SQL {title="REQUIRES_PLAYER_IS_ALLY_LEVEL_1"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_IS_ALLY_LEVEL_1",
		"REQUIREMENT_PLAYER_HAS_ACTIVE_ALLIANCE_OF_AT_LEAST_LEVEL"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_IS_ALLY_LEVEL_1",
		"Level",
		1
	);
	
```
