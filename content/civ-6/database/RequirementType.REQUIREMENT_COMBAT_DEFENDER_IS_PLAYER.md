---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_DEFENDER_IS_PLAYER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_DEFENDER_IS_PLAYER
>
> * Class: `COMBATS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_DEFENDER_IS_EMERGENCY_TARGET"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_DEFENDER_IS_EMERGENCY_TARGET",
		"REQUIREMENT_COMBAT_DEFENDER_IS_PLAYER"
	);


```
