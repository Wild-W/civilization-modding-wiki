---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_PANTHEON
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_PANTHEON
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_PANTHEON"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_PANTHEON",
		"REQUIREMENT_PLAYER_HAS_PANTHEON"
	);


```
