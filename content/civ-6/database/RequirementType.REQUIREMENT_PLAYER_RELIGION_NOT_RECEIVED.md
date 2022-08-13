---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_RELIGION_NOT_RECEIVED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_RELIGION_NOT_RECEIVED
>
> * Class: `PLAYERS`
> * Arguments:
>	* FoundingDelay `Integer`

## Samples

```SQL {title="REQUIRES_RELIGION_NOT_RECEIVED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_RELIGION_NOT_RECEIVED",
		"REQUIREMENT_PLAYER_RELIGION_NOT_RECEIVED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_RELIGION_NOT_RECEIVED",
		"FoundingDelay",
		10
	);
	
```
