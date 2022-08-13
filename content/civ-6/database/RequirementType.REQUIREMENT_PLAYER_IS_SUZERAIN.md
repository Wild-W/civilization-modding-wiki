---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_SUZERAIN
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_SUZERAIN
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_IS_NOT_SUZERAIN"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_IS_NOT_SUZERAIN",
		"REQUIREMENT_PLAYER_IS_SUZERAIN",
		1
	);

```
