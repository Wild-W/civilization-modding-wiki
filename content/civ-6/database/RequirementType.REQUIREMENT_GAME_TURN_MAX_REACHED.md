---
tags:
- RequirementType
title: REQUIREMENT_GAME_TURN_MAX_REACHED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_TURN_MAX_REACHED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="TIME_DEFEAT_MAX_TURN_REACHED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"TIME_DEFEAT_MAX_TURN_REACHED",
		"REQUIREMENT_GAME_TURN_MAX_REACHED"
	);


```
