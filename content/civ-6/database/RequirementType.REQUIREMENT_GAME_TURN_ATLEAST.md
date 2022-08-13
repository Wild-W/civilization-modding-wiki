---
tags:
- RequirementType
title: REQUIREMENT_GAME_TURN_ATLEAST
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_TURN_ATLEAST
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinGameTurn `Integer`
>		* Elapsed turns
>	* AdjustForGameSpeed `Boolean`

## Samples

```SQL {title="REQUIRES_GAME_60_TURNS_IN"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_GAME_60_TURNS_IN",
		"REQUIREMENT_GAME_TURN_ATLEAST"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_GAME_60_TURNS_IN",
		"AdjustForGameSpeed",
		1
	),
	(
		"REQUIRES_GAME_60_TURNS_IN",
		"MinGameTurn",
		60
	);
	```
