---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_BARBARIAN
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_BARBARIAN
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="PLAYER_IS_BARB_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLAYER_IS_BARB_REQUIREMENT",
		"REQUIREMENT_PLAYER_IS_BARBARIAN"
	);

```
