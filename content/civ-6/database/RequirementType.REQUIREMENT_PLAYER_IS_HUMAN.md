---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_HUMAN
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_HUMAN
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_IS_AI"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_IS_AI",
		"REQUIREMENT_PLAYER_IS_HUMAN",
		1
	);

```
