---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_WINNING_ANY_VICTORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_WINNING_ANY_VICTORY
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_EMERGENCY_TARGET_IS_WINNING"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_EMERGENCY_TARGET_IS_WINNING",
		"REQUIREMENT_PLAYER_IS_WINNING_ANY_VICTORY"
	);


```
