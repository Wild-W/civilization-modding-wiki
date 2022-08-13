---
tags:
- RequirementType
title: REQUIREMENT_GAME_ERA_ATLEAST
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_ERA_ATLEAST
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinGameEra `String`

## Samples

```SQL {title="GAME_ERA_LIMIT_REACHED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"GAME_ERA_LIMIT_REACHED",
		"REQUIREMENT_GAME_ERA_ATLEAST"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"GAME_ERA_LIMIT_REACHED",
		"MinGameEra",
		"ERA_INDUSTRIAL"
	);
	```
