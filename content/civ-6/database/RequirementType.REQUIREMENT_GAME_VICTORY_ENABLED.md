---
tags:
- RequirementType
title: REQUIREMENT_GAME_VICTORY_ENABLED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_VICTORY_ENABLED
>
> * Class: `PLAYERS`
> * Arguments:
>	* VictoryType `String`

## Samples

```SQL {title="DEFAULT_VICTORY_DOMINATION_DISABLED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse,
		ProgressWeight
	)
VALUES
	(
		"DEFAULT_VICTORY_DOMINATION_DISABLED",
		"REQUIREMENT_GAME_VICTORY_ENABLED",
		1,
		0
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"DEFAULT_VICTORY_DOMINATION_DISABLED",
		"VictoryType",
		"VICTORY_CONQUEST"
	);
	
```
