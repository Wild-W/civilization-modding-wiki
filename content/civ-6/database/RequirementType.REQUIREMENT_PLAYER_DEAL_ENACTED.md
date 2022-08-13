---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_DEAL_ENACTED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_DEAL_ENACTED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_DEAL_ENACTED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_DEAL_ENACTED",
		"REQUIREMENT_PLAYER_DEAL_ENACTED",
		1
	);

```
