---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_ANGEVIN_EMPIRE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_ANGEVIN_EMPIRE
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomRankingDiploMod `Integer`
>	* HighPopulationThreshold `Integer`
>	* LowPopulationThreshold `Integer`
>	* StatementKey `String`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_ANGEVIN_EMPIRE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_ANGEVIN_EMPIRE",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_ANGEVIN_EMPIRE",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_ANGEVIN_EMPIRE",
		"BottomRankingDiploMod",
		"-8"
	),
	(
		"AGENDA_ANGEVIN_EMPIRE",
		"HighPopulationThreshold",
		110
	),
	(
		"AGENDA_ANGEVIN_EMPIRE",
		"LowPopulationThreshold",
		70
	),
	(
		"AGENDA_ANGEVIN_EMPIRE",
		"StatementKey",
		"AGENDA_ANGEVIN_EMPIRE_WARNING"
	),
	(
		"AGENDA_ANGEVIN_EMPIRE",
		"TopRankingDiploMod",
		8
	);
	
```

