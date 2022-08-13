---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_SAME_SEX
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_SAME_SEX
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_OPPOSITE_SEX"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_OPPOSITE_SEX",
		"REQUIREMENT_PLAYER_IS_SAME_SEX",
		1
	);

```
