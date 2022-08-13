---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_FOUNDED_NO_RELIGION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_FOUNDED_NO_RELIGION
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_FOUNDED_A_RELIGION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_FOUNDED_A_RELIGION",
		"REQUIREMENT_PLAYER_FOUNDED_NO_RELIGION",
		1
	);

```
