---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_WAS_KILLED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_WAS_KILLED
>
> * Class: `COMBATS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_ENEMY_GOT_MURDERATED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_ENEMY_GOT_MURDERATED",
		"REQUIREMENT_OPPONENT_WAS_KILLED"
	);


```
