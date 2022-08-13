---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_ENEMY_NOT_ALLIANCE_RELIGION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_ENEMY_NOT_ALLIANCE_RELIGION
>
> * Class: `COMBATS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_RELIGIOUS_ENEMY_NOT_ALLIED_RELIGION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_RELIGIOUS_ENEMY_NOT_ALLIED_RELIGION",
		"REQUIREMENT_COMBAT_ENEMY_NOT_ALLIANCE_RELIGION"
	);

```
