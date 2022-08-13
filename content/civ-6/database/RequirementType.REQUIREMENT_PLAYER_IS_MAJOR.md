---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_MAJOR
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_MAJOR
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRE_THIS_PLAYER_IS_MAJOR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRE_THIS_PLAYER_IS_MAJOR",
		"REQUIREMENT_PLAYER_IS_MAJOR"
	);


```
