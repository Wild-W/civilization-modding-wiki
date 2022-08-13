---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_CLOSE_TO_VICTORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_CLOSE_TO_VICTORY
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_CLOSE_TO_VICTORY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_CLOSE_TO_VICTORY",
		"REQUIREMENT_PLAYER_IS_CLOSE_TO_VICTORY"
	);


```
