---
tags:
- RequirementType
title: REQUIREMENT_DELEGATION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_DELEGATION
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_DELEGATION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_DELEGATION",
		"REQUIREMENT_DELEGATION"
	);


```
