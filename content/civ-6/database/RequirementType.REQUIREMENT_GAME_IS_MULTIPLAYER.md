---
tags:
- RequirementType
title: REQUIREMENT_GAME_IS_MULTIPLAYER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_GAME_IS_MULTIPLAYER
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="GAME_IS_SP"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"GAME_IS_SP",
		"REQUIREMENT_GAME_IS_MULTIPLAYER",
		1
	);


```
