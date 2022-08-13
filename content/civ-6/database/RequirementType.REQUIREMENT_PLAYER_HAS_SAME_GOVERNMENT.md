---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_SAME_GOVERNMENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_SAME_GOVERNMENT
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_DIFFERENT_GOVERNMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_DIFFERENT_GOVERNMENT",
		"REQUIREMENT_PLAYER_HAS_SAME_GOVERNMENT",
		1
	);

```
