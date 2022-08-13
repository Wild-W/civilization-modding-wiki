---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_DESIRED_LUXURY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_DESIRED_LUXURY
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_HAS_DESIRED_LUXURY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_DESIRED_LUXURY",
		"REQUIREMENT_PLAYER_HAS_DESIRED_LUXURY"
	);


```
