---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_ERA_AT_LEAST
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_ERA_AT_LEAST
>
> * Class: `PLAYERS`
> * Arguments:
>	* EraType `String`
>		* [Eras.EraType]

## Samples

```SQL {title="REQUIRES_PLAYER_IS_INDUSTRIAL_ERA"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_IS_INDUSTRIAL_ERA",
		"REQUIREMENT_PLAYER_ERA_AT_LEAST"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_IS_INDUSTRIAL_ERA",
		"EraType",
		"ERA_INDUSTRIAL"
	);
	
```
