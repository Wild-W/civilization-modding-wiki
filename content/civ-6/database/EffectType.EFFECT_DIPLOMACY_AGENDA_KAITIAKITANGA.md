---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_KAITIAKITANGA
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_KAITIAKITANGA
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* HiddenAgenda `Boolean`
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_ENVIRONMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_ENVIRONMENT",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_KAITIAKITANGA",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_ENVIRONMENT",
		"BottomPercentage",
		40
	),
	(
		"AGENDA_ENVIRONMENT",
		"BottomRankingDiploMod",
		"-6"
	),
	(
		"AGENDA_ENVIRONMENT",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_ENVIRONMENT",
		"StatementKey",
		"AGENDA_KAITIAKITANGA_WARNING"
	),
	(
		"AGENDA_ENVIRONMENT",
		"TopPercentage",
		60
	),
	(
		"AGENDA_ENVIRONMENT",
		"TopRankingDiploMod",
		6
	);
	
```

