---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_AT_PEACE_WITH_ALL_MAJORS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_AT_PEACE_WITH_ALL_MAJORS
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_AT_PEACE_WITH_ALL_MAJORS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_AT_PEACE_WITH_ALL_MAJORS",
		"REQUIREMENT_PLAYER_IS_AT_PEACE_WITH_ALL_MAJORS"
	);


```
