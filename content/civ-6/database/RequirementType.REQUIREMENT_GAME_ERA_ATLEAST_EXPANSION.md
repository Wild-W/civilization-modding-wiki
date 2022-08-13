---
tags:
- RequirementType
title: REQUIREMENT_GAME_ERA_ATLEAST_EXPANSION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_ERA_ATLEAST_EXPANSION
>
> * Class: `PLAYERS`
> * Arguments:
>	* EraType `String`
>		* [Eras.EraType]

## Samples

```SQL {title="REQUIRES_ERA_ATLEASTEXPANSION_ATOMIC"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_ERA_ATLEASTEXPANSION_ATOMIC",
		"REQUIREMENT_GAME_ERA_ATLEAST_EXPANSION"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_ERA_ATLEASTEXPANSION_ATOMIC",
		"EraType",
		"ERA_ATOMIC"
	);
	```
