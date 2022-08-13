---
tags:
- RequirementType
title: REQUIREMENT_GAME_ERA_ATMOST_EXPANSION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_ERA_ATMOST_EXPANSION
>
> * Class: `PLAYERS`
> * Arguments:
>	* EraType `String`

## Samples

```SQL {title="REQUIRES_GAME_ERA_BEFORE_ATOMIC"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_GAME_ERA_BEFORE_ATOMIC",
		"REQUIREMENT_GAME_ERA_ATMOST_EXPANSION"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_GAME_ERA_BEFORE_ATOMIC",
		"EraType",
		"ERA_MODERN"
	);
	
```
