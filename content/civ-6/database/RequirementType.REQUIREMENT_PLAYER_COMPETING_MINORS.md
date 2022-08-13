---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_COMPETING_MINORS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_COMPETING_MINORS
>
> * Class: `PLAYERS`
> * Arguments:
>	* PercentCompeting `Integer`

## Samples

```SQL {title="REQUIRES_COMPETING_MINORS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_COMPETING_MINORS",
		"REQUIREMENT_PLAYER_COMPETING_MINORS"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_COMPETING_MINORS",
		"PercentCompeting",
		50
	);
	
```
