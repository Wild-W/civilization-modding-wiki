---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_SAME_RELIGION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_SAME_RELIGION
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_SAME_RELIGION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_SAME_RELIGION",
		"REQUIREMENT_PLAYER_IS_SAME_RELIGION"
	);


```
