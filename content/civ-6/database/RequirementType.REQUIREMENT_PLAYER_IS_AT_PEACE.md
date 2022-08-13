---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_AT_PEACE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_AT_PEACE
>
> * Class: `PLAYERS`
> * Arguments:
>	* Min Turns `Integer`

## Samples

```SQL {title="REQUIRES_AT_PEACE_10_TURNS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_AT_PEACE_10_TURNS",
		"REQUIREMENT_PLAYER_IS_AT_PEACE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_AT_PEACE_10_TURNS",
		"Min Turns",
		10
	);
	
```

```SQL {title="REQUIRES_PLAYER_AT_PEACE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_AT_PEACE",
		"REQUIREMENT_PLAYER_IS_AT_PEACE"
	);


```
