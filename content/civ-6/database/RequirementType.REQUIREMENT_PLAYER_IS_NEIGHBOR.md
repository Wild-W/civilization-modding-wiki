---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_NEIGHBOR
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_NEIGHBOR
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_NEIGHBOR_CIVS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_NEIGHBOR_CIVS",
		"REQUIREMENT_PLAYER_IS_NEIGHBOR"
	);


```