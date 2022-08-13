---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_MET_X_TURNS_AGO
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_MET_X_TURNS_AGO
>
> * Class: `PLAYERS`
> * Arguments:
>	* TurnsAgo `Integer`

## Samples

```SQL {title="REQUIRES_MET_10_TURNS_AGO"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_MET_10_TURNS_AGO",
		"REQUIREMENT_PLAYER_MET_X_TURNS_AGO"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_MET_10_TURNS_AGO",
		"TurnsAgo",
		10
	);
	
```
