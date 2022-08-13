---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_MAJORITY_RELIGION_IS_OWNER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_MAJORITY_RELIGION_IS_OWNER
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="RELIGIOUS_VICTORY_MAJORITY_RELIGION_IS_OWNER_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"RELIGIOUS_VICTORY_MAJORITY_RELIGION_IS_OWNER_REQUIREMENT",
		"REQUIREMENT_PLAYER_MAJORITY_RELIGION_IS_OWNER"
	);

```
