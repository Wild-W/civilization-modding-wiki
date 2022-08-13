---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_EMERGENCY_TARGET
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_EMERGENCY_TARGET
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_IS_EMERGENCY_MEMBER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_IS_EMERGENCY_MEMBER",
		"REQUIREMENT_PLAYER_IS_EMERGENCY_TARGET",
		1
	);


```
