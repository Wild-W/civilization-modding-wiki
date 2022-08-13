---
tags:
- RequirementType
title: REQUIREMENT_GAME_CLIMATE_CHANGE_LEVEL_AT_LEAST
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_CLIMATE_CHANGE_LEVEL_AT_LEAST
>
> * Class: `PLAYERS`
> * Arguments:
>	* Amount `Integer`

## Samples

```SQL {title="CLIMATE_LEVEL_AT_LEAST_8"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"CLIMATE_LEVEL_AT_LEAST_8",
		"REQUIREMENT_GAME_CLIMATE_CHANGE_LEVEL_AT_LEAST"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"CLIMATE_LEVEL_AT_LEAST_8",
		"Amount",
		8
	);
	
```
